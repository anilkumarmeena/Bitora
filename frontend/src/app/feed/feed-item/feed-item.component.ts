import {Component, Input, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import { jason } from '../feed.component';

@Component({
  selector: 'app-feed-item',
  templateUrl: './feed-item.component.html',
})
export class FeedItemComponent implements OnInit {

  @Input() data : any[];

  constructor(private route: Router) { }

  ngOnInit() {
    console.log(this.data);

  }

  openAnswerView() {
    this.route.navigate(['feed', 'answers', '347878377474784374378']);
  }
}


