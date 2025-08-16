document.addEventListener('DOMContentLoaded', function() {
    const tableBody = document.getElementById('tableBody');
    const refreshBtn = document.getElementById('refreshBtn');
    const lastUpdateElement = document.getElementById('lastUpdate');
    
    // Elementos do resumo
    const totalStudentsElement = document.getElementById('totalStudents');
    const approvedStudentsElement = document.getElementById('approvedStudents');
    const failedStudentsElement = document.getElementById('failedStudents');
    const averageGradeElement = document.getElementById('averageGrade');

    function formatDateTime(date) {
        return new Intl.DateTimeFormat('pt-BR', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }).format(date);
    }

    function updateLastUpdateTime() {
        const now = new Date();
        lastUpdateElement.textContent = `Última atualização: ${formatDateTime(now)}`;
    }

    async function fetchGrades() {
        try {
            // Adiciona um timestamp para evitar cache
            const response = await fetch('notas.json?t=' + new Date().getTime());
            
            if (!response.ok) {
                throw new Error('Erro ao carregar dados');
            }
            
            const data = await response.json();
            renderTable(data);
            updateSummary(data);
            updateLastUpdateTime();
        } catch (error) {
            console.error('Erro:', error);
            tableBody.innerHTML = `<tr><td colspan="7" class="error">Erro ao carregar dados. Verifique se o servidor está rodando.</td></tr>`;
        }
    }

    function renderTable(data) {
        if (!data || data.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="7">Nenhum dado disponível. Cadastre alunos no sistema Python.</td></tr>`;
            return;
        }

        tableBody.innerHTML = data.map(student => `
            <tr>
                <td>${student.Aluno}</td>
                <td>${student.Bimestre1.toFixed(1)}</td>
                <td>${student.Bimestre2.toFixed(1)}</td>
                <td>${student.Bimestre3.toFixed(1)}</td>
                <td>${student.Bimestre4.toFixed(1)}</td>
                <td><strong>${student.Média.toFixed(1)}</strong></td>
                <td>
                    <span class="status ${student.Média >= 7 ? 'approved' : 'failed'}">
                        ${student.Média >= 7 ? 'Aprovado' : 'Reprovado'}
                    </span>
                </td>
            </tr>
        `).join('');
    }

    function updateSummary(data) {
        const total = data.length;
        const approved = data.filter(student => student.Média >= 7).length;
        const failed = total - approved;
        const average = total > 0 
            ? (data.reduce((sum, student) => sum + student.Média, 0) / total).toFixed(1)
            : 0;

        totalStudentsElement.textContent = total;
        approvedStudentsElement.textContent = approved;
        failedStudentsElement.textContent = failed;
        averageGradeElement.textContent = average;
    }

    // Carrega os dados inicialmente
    fetchGrades();

    // Configura o botão de atualização
    refreshBtn.addEventListener('click', fetchGrades);

    // Atualiza automaticamente a cada 30 segundos
    setInterval(fetchGrades, 30000);
});