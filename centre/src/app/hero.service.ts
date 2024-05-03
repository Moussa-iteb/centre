import { Injectable } from '@angular/core';
import axios from 'axios';
@Injectable({
  providedIn: 'root'
})
export class HeroService {

  constructor() { }
  
  async addFile(data: any){
    return await axios.post('http://127.0.0.1:8000/addfile',data)
  }

  async add(data: any){
    return await axios.post('http://127.0.0.1:8000/add',data)
  }

  async ajouter(data: any){
    return await axios.post('http://127.0.0.1:8000',data)
  }
  async addutilisateur(data:any){
    return await axios.post('http://127.0.0.1:8000/admin',data);
  }
  async  get(id: any){
    return await  axios.get('http://127.0.0.1:8000/admin'+id,{});
  }

  async getUtilisateur(){
    return await axios.get('http://127.0.0.1:8000/admin',{});
  }
}

