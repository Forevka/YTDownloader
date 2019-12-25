import uvicorn
from app import app
import handlers.get_video_quality


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
