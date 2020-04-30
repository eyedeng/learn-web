// 访问时恢复加密内容，除了加密文件，好像还可躲审查

window.onload = function(){
    const key = parseInt(prompt("key number:", 0));
    const zh_sta = 0x4e00; 
    const zh_end = 0x9fa5 + key;

    let no_code_part = false  // 非加密部分 标志
    const no_code_s = 8594; 
    const no_code_e = 8592;

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
                if(!no_code_part && n >= zh_sta && n <= zh_end){
                    t += String.fromCharCode(n - key);
                }else if(n == no_code_s || n == no_code_e){
                    if(n == no_code_s){
                        no_code_part = true;
                    }else{
                        no_code_part = false;
                    }
                }
                else{
                    t += code[i];
                }
            }
            node.textContent = t;
        }
    }
    dfs(root);
}