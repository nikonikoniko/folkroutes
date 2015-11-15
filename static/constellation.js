

nids = [
{"num":0,"name":"Folkroutes","charge":1000}
    {% for item in floatsam %}
        ,{
          "num":{{item.floatsam_id}},
          "name":"{{item.name}}",
          "url":"/floatsam/json/{{item.floatsam_id}}",
          "charge":{{item.charge}},
        }
    {% endfor %}
  ]
var graph = {
  nodes: nids,
  links: [
    {% for item in floatsam %}
      {% for thing in item.peers  %}
        {source:  {{item.floatsam_id}}, target:  {{thing.floatsam_id}}},
      {% endfor %}
    {% endfor %}


  ]
};


var width = document.getElementById("viz").offsetWidth,
    height = document.getElementById("viz").offsetHeight;

var spincenter_x = width/2;
var spincenter_y = height/2;



var t0 = Date.now();
var state_rotate = 90 + t0 * 1/200;
var state_translate = [0,0]
var state_scale = 1




var zoomListener = d3.behavior.zoom()
  .scaleExtent([1, 10])
  .on("zoom", redraw);


var momsvg = d3.select("viz").append("svg:svg")
    .attr("width", width)
    .attr("height", height)
    .call(zoomListener)
    .attr("pointer-events", "all")
  .append('svg:g')
  .attr("width", width)
    .attr("height", height)
  .attr("id","mom");




var svg = momsvg.append("g")
    .attr("width", width)
    .attr("height", height)
    .attr("id","svg");

var force = d3.layout.force()
    .size([width, height])
    .friction(.9)
    .linkStrength(0.3)
    .charge(function(d){
      console.log(d.charge);
      return d.charge;
      })
    .gravity(.3)
    .theta(0.8)
    .alpha(0.1)
    .on("tick", tick);





  var gnodes = svg.selectAll('g.gnode')
     .data(graph.nodes)
     .enter()
     .append('g')
     .classed('gnode', true)
     .on('mouseover', function(d){
        var nodeSelection = d3.select(this).style({opacity:'0.8'});
        nodeSelection.select("text").style({opacity:'1.0'});
      })
     .on('mouseout', function(d){
        var nodeSelection = d3.select(this).style({opacity:'1.0'});
        nodeSelection.select("text").style({opacity:'0.1'});
      });


  var link = svg.selectAll(".link")
      .data(graph.links)
      .enter()
      .append("line")
      .attr("class", "link")
      .style("stroke-width", .2);


    var node = gnodes.append("circle")
      .attr("class", "node")
      .attr("r", 1.5)
      .style("fill", function(d) { return "#fff" });

  var labels = gnodes.append("text")
      .text(function(d) { return d.name; })
      .style('fill', 'white')
      .style("font-size", "6px")
      .style({opacity:'0.1'})
      .on("click",function(d){
        ajax_link_clicked(d.url);

        scale = 2;


        tx= width/2+ -scale*d.x;
        ty= height/2+ -scale*d.y;


        spincenter_x = d.x;
        spincenter_y = d.y;


      zoomListener.scale(scale).translate([tx,ty]);

      var T = momsvg.transition().duration(20)
      zoomListener.event(T);
      })
      .style("cursor","pointer");


var drawGraph = function(graph) {



  force
      .nodes(graph.nodes)
      .links(graph.links)
      .start();




}


drawGraph(graph);









function redraw() {


  state_translate = d3.event.translate;
  state_scale = d3.event.scale;
  momsvg.attr("transform", "translate(" + state_translate + ")"
      + " scale(" + state_scale + ")"
      );

}











function tick() {
  link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    gnodes.attr("transform", function(d) {
        return 'translate(' + [d.x, d.y] + ')';
    });

    console.log("sup");
}











  d3.timer(function() {
    var delta = (Date.now() - t0);

    state_rotate = 0 + delta * 1/900;

    svg.attr("transform", "rotate(" + state_rotate + "," + spincenter_x +"," + spincenter_y +")");
    // zoomListener.rotate([state_rotate,spincenter_x,spincenter_y]).transition();
    labels.attr("transform", "rotate(" + -1 * state_rotate +")");



    //momsvg.attr("transform", " translate(" + state_translate + ")"
      //+ " scale(" + state_scale + ")")
  });












  $("#infomain").hide();



  function ajax_link_clicked(url){
    console.log("clocle" + url);

    $.getJSON(url, function(data) {
      console.log(data);
      console.log(data.name);
      var template = _.template($("#infotemplate").html());
      $("#infomain").html(template(data)).show();
    });


  }








