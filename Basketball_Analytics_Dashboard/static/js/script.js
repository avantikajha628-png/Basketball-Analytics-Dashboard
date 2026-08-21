// Basketball Analytics Dashboard - Frontend Logic

document.addEventListener("DOMContentLoaded", () => {
  loadDashboardCards();
  loadTopPlayersChart();
  loadPositionChart();
  loadPlayersTable();
  setupSidebarToggle();
});

// Load dashboard stats
function loadDashboardCards() {
  fetch("/api/dashboard")
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("totalPlayers").textContent = data.total_players;
      document.getElementById("totalTeams").textContent = data.total_teams;
      document.getElementById("totalGames").textContent = data.total_games;
      document.getElementById("avgPoints").textContent = data.avg_points;
    })
    .catch((err) => console.error("Error loading dashboard cards:", err));
}

// Load top scorers chart
function loadTopPlayersChart() {
  fetch("/api/top-players")
    .then((res) => res.json())
    .then((data) => {
      const ctx = document.getElementById("topPlayersChart").getContext("2d");

      const gradient = ctx.createLinearGradient(0, 0, 0, 340);
      gradient.addColorStop(0, "#ff7a00");
      gradient.addColorStop(1, "#6d5dfc");

      // Shorten labels to fit on axis
      const shortLabels = data.labels.map((name) => {
        const parts = name.split(" ");
        return parts.length > 1 ? `${parts[0][0]}. ${parts[parts.length - 1]}` : name;
      });

      new Chart(ctx, {
        type: "bar",
        data: {
          labels: shortLabels,
          datasets: [
            {
              label: "Total Points",
              data: data.data,
              backgroundColor: gradient,
              borderRadius: 8,
              maxBarThickness: 34,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          aspectRatio: 1.8,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                title: (items) => data.labels[items[0].dataIndex],
              },
            },
          },
          scales: {
            x: {
              ticks: {
                color: "#94a3b8",
                font: { family: "Poppins", size: 11 },
                autoSkip: false,
                maxRotation: 40,
                minRotation: 40,
              },
              grid: { display: false },
            },
            y: {
              ticks: { color: "#94a3b8", font: { family: "Poppins" } },
              grid: { color: "rgba(255,255,255,0.06)" },
            },
          },
        },
      });
    })
    .catch((err) => console.error("Error loading top players chart:", err));
}

// Load position distribution chart
function loadPositionChart() {
  fetch("/api/player-position")
    .then((res) => res.json())
    .then((data) => {
      const ctx = document.getElementById("positionChart").getContext("2d");

      new Chart(ctx, {
        type: "pie",
        data: {
          labels: data.labels,
          datasets: [
            {
              data: data.data,
              backgroundColor: ["#ff7a00", "#6d5dfc", "#22c55e", "#64748b"],
              borderColor: "#111827",
              borderWidth: 3,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          aspectRatio: 1.4,
          plugins: {
            legend: {
              position: "bottom",
              labels: { color: "#e5e7eb", font: { family: "Poppins" } },
            },
          },
        },
      });
    })
    .catch((err) => console.error("Error loading position chart:", err));
}

// Load player stats table
function loadPlayersTable() {
  fetch("/api/players")
    .then((res) => res.json())
    .then((players) => {
      const tbody = document.getElementById("playersTableBody");
      tbody.innerHTML = "";

      // Show top 10 players
      const topPlayers = players.slice(0, 10);

      topPlayers.forEach((p) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${p.player_name}</td>
          <td>${p.team}</td>
          <td><span class="position-badge ${p.position}">${p.position}</span></td>
          <td>${p.points}</td>
          <td>${p.assists}</td>
          <td>${p.field_goal}%</td>
        `;
        tbody.appendChild(row);
      });
    })
    .catch((err) => console.error("Error loading players table:", err));
}

// Sidebar toggle for mobile
function setupSidebarToggle() {
  const toggleBtn = document.getElementById("sidebarToggle");
  const sidebar = document.getElementById("sidebar");

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("show");
    });
  }

  // Update active link and close sidebar on mobile
  document.querySelectorAll(".sidebar-menu a").forEach((link) => {
    link.addEventListener("click", () => {
      document.querySelectorAll(".sidebar-menu a").forEach((l) => l.classList.remove("active"));
      link.classList.add("active");
      if (window.innerWidth < 992) {
        sidebar.classList.remove("show");
      }
    });
  });
}
