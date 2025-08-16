// Aguarda o DOM ser totalmente carregado
document.addEventListener('DOMContentLoaded', function() {
  // Seleciona todos os links de navegação
  const navLinks = document.querySelectorAll('.nav-link');
  
  // Adiciona evento de clique a cada link
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault(); // Previne o comportamento padrão
      
      // Obtém o nome da página em minúsculas
      const pageName = this.textContent.toLowerCase();
      
      // Redireciona para a página correspondente
      window.location.href = `Pages/${pageName}.html`;
    });
  });
});
