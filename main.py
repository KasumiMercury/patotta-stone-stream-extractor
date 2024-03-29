import functions_framework
from yt_dlp import YoutubeDL

@functions_framework.http
def function(request):
    vid = request.args.get('vid')
    # If vid is not provided, report an error
    if vid is None:
        raise RuntimeError("No vid provided")
    
    stream = extract_stream(vid)
    stream_url = stream.get("url")
    
    return stream_url

def extract_stream(vid):
    # Extract video streams metadata from Youtube
    target = f"https://www.youtube.com/watch?v={vid}"
    stream_meta = YoutubeDL().extract_info(target, download=False).get('formats', {})
    
    # Extract and filter out the streams that we want
    streams = {}
    for stream in stream_meta:
        stream_res = stream.get("width", "")
        stream_url = stream.get("url", "")
        stream_protocol = stream.get("protocol", "")
        stream_with_video = (
            False if stream.get("vcodec", "none") == "none" else True
        )
        stream_with_audio = (
            False if stream.get("acodec", "none") == "none" else True
        )
        stream_fps = stream.get("fps", "")
        
        if not (stream_with_video and stream_res and stream_url and stream_protocol == "m3u8_native"):
            continue
        if stream_with_audio:
            continue
        
        streams[stream_res] = {
            "url": stream_url,
            "protocol": stream_protocol,
            "fps": int(stream_fps) if stream_fps else None,
            "width": stream_res,
        }

    # sort streams by key
    streams = dict(sorted(streams.items(), reverse=True))
    
    # find the highest resolution stream
    best_stream = streams[list(streams.keys())[0]]
    
    return best_stream
