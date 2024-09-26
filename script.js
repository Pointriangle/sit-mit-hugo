const bouton = document.getElementById(btn-f);
document.addEventListener('mousemove'),(souris)=>{}
const rect =bouton.getBoundingClientRect();
const distance = math.sqrt(Math.pow(souris.clientX-(rect.left+rect.width/2),2))+Math.pow(souris.clientY-(rect.top+rect.height/2),2);
if (distance<100){const newTop = math.random()*(window.innerHeight-rect.height);
    const newLeft=math.random()*(window.innerWidth - rect.width);
    bouton.style.top = newTop + 'px';
    bouton.style.left = newLeft +'px';
}