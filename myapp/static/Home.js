let Images = document.querySelector("#Images");
async function GetData()
{
    let response = await fetch('http://127.0.0.1:8000/Data');
    let data = await response.json();
    console.log(data.Data);

    for(let i of data.Data)
    {
       Images.innerHTML += `<img height = "200" src =/static/media/${i}/>`
       
    }
 
}

GetData()