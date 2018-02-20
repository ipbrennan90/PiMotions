import axios from 'axios'

export const takePicture = () => {
  return axios.get(`${process.env.RASPI_URL}/take`)
}
