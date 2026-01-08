"use client";

import { projectsData } from "@/lib/data";
import Project from "@/components/project";
import { useSectionInView } from "@/lib/hooks";

export default function Projects() {
  const { ref } = useSectionInView("Projects", 0.5);

  return (
    <section ref={ref} id="projects" className="scroll-mt-28 mb-28">
      <h2 className="text-3xl font-medium capitalize mb-8 text-center">Mes Projets</h2>
      <div>
        {projectsData.map((project, index) => (
            <>
            <Project {...project} />
          </>
        ))}
      </div>
    </section>
  );
}