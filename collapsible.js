let arrows = document.querySelectorAll('img[alt="arrow.down"]');
Array.from(arrows).forEach(arrow => {
  let title = arrow.parentNode;
  let container = title.parentNode.querySelectorAll('div')[1];
  container.style.overflow = 'hidden';
  container.style.height = '0px';
  container.style.transition = '0.2s'
  arrow.style.transform = 'rotate(90deg)';
  arrow.style.transition = '0.2s'

  title.addEventListener('click', () => {
    if (String(container.style.height) === '0px') {
      arrow.style.transform = '';
      container.style.height = ''
      container.style.overflow = '';
    } else {
      arrow.style.transform = 'rotate(90deg)';
      container.style.height = '0px'
      container.style.overflow = 'hidden';
    }
  });
});