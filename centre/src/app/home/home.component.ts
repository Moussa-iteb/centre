import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.sass']
})

export class HomeComponent implements OnInit {

  constructor(public router: Router,public heroService:HeroService) { }

  ngOnInit(): void {
  }
  logMeOut() {
    this.router.navigateByUrl('login');
  }
}
