import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HeroService } from '../hero.service';
import { ActivatedRoute } from '@angular/router';
import { Message } from '@angular/compiler/src/i18n/i18n_ast';
class admin {
  static email:any;
   static nom:any;
    static Password:any;
  }

  

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.sass']
})
export class LoginComponent implements OnInit {
admin:any;
email:any;
password:any;
nom:any;
id:any;
connexion:any;

  constructor(private heroService:HeroService,private activatedRoute: ActivatedRoute,private router: Router) { }

  ngOnInit(): void {
  }
  login(connexion:any){
    let med={email:'',password:''};
   med.email=connexion.email;
   med.password = connexion.password;
   console.log(med)
   this.heroService.get(med).then(
     Response=>{
       console.log(Response)
       if(Response.data.msg=="erreur"){
alert("erreur");
       }else{
        localStorage.setItem('tokenMed',Response.data.tokenMed);
        this.router.navigate(['/dashboard/home']);
       }
     
     }
    );
    
 }
  
      }

