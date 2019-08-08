import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ranking',
  templateUrl: './ranking.component.html',
  styleUrls: ['./ranking.component.css']
})
export class RankingComponent implements OnInit {
  dataSubmitted = {name: '', rank: 0}
  dataToDisplay = {}
  dataRanks = [{name: 'Emma', score: 100}, {name: 'David', score: 100}, {name: 'Caroline', score: 50}]
  ids = [1, 1, 2,3]
  constructor() { }



  ngOnInit() {
  }

  initArray (n:number) {
   
      var arr = Array.apply(1, Array(n));
      return arr.map(function (x, i) { return 1 });
  
  }
  rank_a_list() {
  
    
    //YOur code here




    
  }

 
}
