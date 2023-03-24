import axios from 'axios';

const local = 'http://localhost:3500'
const aws = "http:///54.233.129.141:3500"

export default axios.create({
    baseURL: local
});