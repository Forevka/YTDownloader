import uvicorn
from app import app
from utils.patch import patch; patch()
import handlers.get_video_quality


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
