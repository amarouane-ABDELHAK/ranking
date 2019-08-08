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
  
    
    this.dataRanks.push({name: this.dataSubmitted.name, score: this.dataSubmitted.rank })

    this.dataRanks.sort(function(first, second) {
      return second.score - first.score;
     });
    let all_scores = []
    this.dataRanks.forEach(element => {
      all_scores.push(element['score'])
    });
    let uniqueScores = all_scores.filter(function(elem, pos) {
      return all_scores.indexOf(elem) == pos;
  })
  
  this.ids = this.initArray(all_scores.length)
  console.log(this.ids)
  var _this = this

  all_scores.forEach(function (value, i) {
    uniqueScores.forEach(element => {
      if(value < element) {
        _this.ids[i] += 1
        return
      }
      
    });
    
});
  //   for i, n_2 in enumerate(list_to_be_ranked):
  //       for n_1 in temp_list:
  //           if n_2 < n_1:
  //               rank[i] += 1
  //               continue
  //   return rank




    
  }

 
}
