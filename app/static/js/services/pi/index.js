import axios from 'axios'
export default class Pi {
    constructor() {
        this.piUrl = process.env.RASPI_URL
    }
    
    takePicture() {
        return axios.get(`${this.piURL}/take`)
    }
}
    
