# SmartCut Luxury

A full-stack web application built with React, FastAPI, and MongoDB. This is a luxury business website with a modern frontend and robust backend.

## 📋 What's Included

✅ React frontend code  
✅ FastAPI backend code  
✅ MongoDB configuration  
✅ Package dependencies (package.json, requirements.txt)  
✅ Project structure and folders  
✅ Configuration files  

## 🚀 Quick Start

### Prerequisites
- Node.js (v14 or higher)
- Python 3.8+
- MongoDB (local or cloud Atlas)
- Git

### Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

The frontend will run on `http://localhost:3000`

### Backend Setup (FastAPI)

```bash
cd backend
pip install -r requirements.txt
python main.py
```

The backend will run on `http://localhost:8000`

### Environment Variables

Create a `.env` file in the backend folder:

```
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=smartcut_luxury
API_HOST=localhost
API_PORT=8000
CORS_ORIGINS=["http://localhost:3000"]
```

For MongoDB Atlas (cloud):
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/smartcut_luxury
```

## 📁 Project Structure

```
smarcut-luxury/
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── .env
├── backend/
│   ├── models/
│   ├── routes/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
└── README.md
```

## 🗄️ Database Setup

### Local MongoDB
```bash
# Install MongoDB and start the service
mongod
```

### MongoDB Atlas (Cloud - Recommended)
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free account
3. Create a cluster
4. Get your connection string
5. Add it to your `.env` file

## 🔌 API Endpoints

The backend provides REST APIs for:
- User management
- Business operations
- Data management

Full API documentation available at `http://localhost:8000/docs` when running the backend.

## 📦 Deployment

### Deploy Frontend (React)
- **Vercel**: `vercel deploy`
- **Netlify**: Push to GitHub, connect Netlify
- **Google Cloud**: Follow Google Cloud deployment guide

### Deploy Backend (FastAPI)
- **Railway.app**: Connect GitHub repo
- **Render.com**: Connect GitHub repo
- **Google Cloud Run**: Push Docker image
- **Heroku**: Using Procfile

### Deploy Database (MongoDB)
- Use MongoDB Atlas (free tier available)
- Or self-host on your server

## 🛠️ Development

### Running in Development Mode

Terminal 1 (Frontend):
```bash
cd frontend
npm start
```

Terminal 2 (Backend):
```bash
cd backend
python main.py
```

Visit `http://localhost:3000` in your browser.

## 📚 Additional Resources

- [React Documentation](https://react.dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [MongoDB Documentation](https://docs.mongodb.com)
- [Axios (HTTP Client)](https://axios-http.com)

## 👥 Support

For questions or issues, please open an issue on GitHub or contact the development team.

---

**Ready to deploy?** Follow the deployment instructions above to get your website live!