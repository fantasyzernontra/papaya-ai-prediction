import Axios from 'axios'

const instance = Axios.create({ baseURL: process.env.REACT_APP_API_BASE_ENDPOINT })

export default instance
