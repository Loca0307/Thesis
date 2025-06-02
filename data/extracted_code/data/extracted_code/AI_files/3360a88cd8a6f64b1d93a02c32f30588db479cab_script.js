
    listItem.id = `noteId-${noteId}`;
    noteId++;
}


function selectNote(x){
      

      for(let i=0;i<x.length;i++){
            x[i].addEventListener("click",function(){
                x[i].style.backgroundColor="rgb(166, 245, 192)";
                // console.log(x[i].children);
            });
      }