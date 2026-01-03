import React from "react";
import { CgWorkAlt } from "react-icons/cg";
import { LuGraduationCap } from "react-icons/lu";


export const links = [
  {
    name: "Accueil",
    hash: "#home",
  },
  {
    name: "Projets",
    hash: "#projects",
  },
  {
    name: "Compétences",
    hash: "#skills",
  },
  {
    name: "Expérience",
    hash: "#experience",
  },
  {
    name: "Contact",
    hash: "#contact",
  },
] as const;

export const experiencesData = [
  {
    title: "Stage Développeur Web",
    location: "ASSOCIATION Jean-Luc François, Pantin, Île-de-France",
    description:
      "Collaborer avec trois collègues à la création et à l'amélioration des sites web de l'association. Développement de fonctionnalités comme un système d'inscription à une newsletter, optimisation des performances (cache), amélioration du responsive design et conception de visuels pour les réseaux sociaux. Développement d'interfaces web, front et back.",
    icon: React.createElement(CgWorkAlt), // À adapter selon vos icônes disponibles
    date: "02/2025 - 03/2025",
  },
  {
    title: "Stage Full Stack Développeur Junior",
    location: "PERFORM VISION, Stains, Île-de-France",
    description:
      "Modernisation de la gestion des bons de livraison via un site extranet dynamique. Discussion avec le client pour établir les besoins et fixer le cahier des charges. Développement de fonctionnalités back-end avec PHP et PostgreSQL, gestion de la base de données utilisateurs. Développement d'interfaces web front et back en utilisant l'architecture MVC et la méthode agile.",
    icon: React.createElement(CgWorkAlt), // À adapter selon vos icônes disponibles
    date: "02/2024 - 03/2024",
  },
  {
    title: "Bénévole Technicien de Maintenance",
    location: "Association LAN.EST.PARTY",
    description:
      "Collaboration avec une équipe de 8 personnes. Gestion et déploiement d'un parc mobile de 12 setups gaming (PC, clavier, souris, casque) pour des tournois e-sport. Organisation de tournois.",
    icon: React.createElement(LuGraduationCap), // À adapter selon vos icônes disponibles
    date: "01/2019 - 01/2022",
  },
] as const;

export const projectsData = [
  {
    title: "Portfolio",
    description:
      "Ce portfolio",
    tags: ["React", "Next.js", "TailwindCSS","Framer-Motion"],
    imageUrl:"",
  },
  {
    title: "Vapeur",
    description:
      "Une application mobile permettant la recommandation d'éléments à l'utilisateur sans qu'il n'ait besoin de se connecter.",
    tags: ["React Native", "SQLite","AsyncStorage"],
    imageUrl: "",
  },
   {
    title: "Horizon",
    description:
      "Une application web complète qui simplifie la gestion de projets pour les équipes. Interface intuitive et outils puissants pour planifier, suivre et livrer des projets efficacement.",
    tags: ["React", "MongoDB", "Laravel", "PHP"],
    imageUrl: "",
  },
] as const;

export const skillsData = {
  langages: [
    "C/C++",
    "Java/JEE", 
    "Python",
    "PHP",
    "TypeScript",
    "JavaScript",
    "XML",
    "HTML5",
    "CSS3"
  ],
  frameworks: [
    "Spring Boot",
    "Laravel",
    "Inertia.js",
    "React",
    "React Native",
    "Vue.js",
    "Express.js",
    "JSP",
    "JUnit",
    "Mockito"
  ],
  architectures: [
    "Architecture Microservices",
    "Architecture trois tiers",
    "Architecture Client-Serveur",
    "API REST",
    "Design Patterns"
  ],
  BDD: [
    "PostgreSQL",
    "MySQL",
    "Redis",
    "MongoDB",
    "SQLite",
    "AsyncStorage"
  ],
  devops: [
    "Docker",
    "Jenkins",
    "Git",
    "Tomcat",
    "Bash/Linux",
    "CI/CD",
    "GitHub",
    "GitLab"
  ],
  méthodologies: [
    "Méthode Agile (SCRUM)",
    "TDD (Test-Driven Development)",
    "Principes SOLID"
  ]
} as const;