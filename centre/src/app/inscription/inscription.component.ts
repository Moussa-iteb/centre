import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { HeroService } from '../hero.service';
class  utilisateur {

}
@Component({
  selector: 'app-inscription',
  templateUrl: './inscription.component.html',
  styleUrls: ['./inscription.component.sass']
})
export class InscriptionComponent implements OnInit {

  constructor(private heroService:HeroService,private activatedRoute : ActivatedRoute,private router:Router) { }

  ngOnInit(): void {
  }
  addutilisateur(liste:any) {
    this.heroService.addutilisateur(liste).then(response=> {
      console.log(response)
    })
    console.log(liste);
    this.router.navigateByUrl('dashboard/home');
}
}