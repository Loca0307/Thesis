console.log(result);







const names=['Mehedi','Mira','Aboni','Aboni','Nid'];
function getLitteone(words){
    let shortname=names[0];
    for(const name of words){
        if(name.length<shortname.length){
            shortname=name;
            
        }
    }
    return shortname;
}

const resut= getLitteone(names);
console.log(resut);