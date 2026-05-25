import axios from "axios";

const API = axios.create({
  baseURL: "https://breathe-esg-backend-8b2s.onrender.com/api",
});

export default API;