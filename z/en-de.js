window.onload = function(){
    
    const key = parseInt(prompt("key number:", 0));
    const zh_sta = 0x4e00; 
    const zh_end = 0x9fa5 + key;

    // let root = $("body").firstElementChild;
    let root = document.getElementsByTagName("body")[0].firstElementChild
    function dfs(node){
        if(node.nodeType == 1){
            for(let i=0; i<node.childNodes.length; i++){  // childNodes:包括text
                dfs(node.childNodes[i]) 
            }
        }
        else if(node.nodeType == 3){    // text
            let code = node.textContent,t = "";
            for(let i=0; i<code.length; i++){
                let n = code.charCodeAt(i);
                if(n >= zh_sta && n <= zh_end){
                    t += String.fromCharCode(n - key);
                }else{
                    t += code[i];
                }
            }
            node.textContent = t;
        }
    }
    dfs(root);
}