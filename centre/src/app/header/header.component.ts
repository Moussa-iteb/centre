import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.sass']
})
export class HeaderComponent implements OnInit {

  constructor(public router: Router,public heroService:HeroService ) { }

  ngOnInit(): void {
  }

  redirectToHome() {
    this.router.navigateByUrl('dashboard/home');
  }
 
  logMeOut() {
    this.router.navigateByUrl('login');
  }
 
  redirectToAbout() {
    this.router.navigateByUrl('dashboard/about');
  }
 
 
 
 
  add(data:any){
    var fileName = data.filename.replace("C:\\fakepath\\", "");
    this.heroService.add({name:fileName}).then((result)=>{
      console.log(result)
    })
  }
  addTwo(data:any){
    var fileName = data.filename.replace("C:\\fakepath\\", "");
    this.heroService.addFile({name:fileName}).then((result)=>{
      console.log(result)
    })
   
  }


}
