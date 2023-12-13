package labyrinthe.core.objets;

public abstract class Objet 
{
    public String nom;
    // l'objet avant avait un id mais cela n'avait pas vraiment d'intérêt
    
    public Objet()
    {
        this.nom = "Guide de survie de l'étudiant en BUT"; // très utile pour la première année ^^
    }

    public Objet(String nom)
    {
        this.nom = nom;
    }

    // set/get Nom
    public void setNom(String nom)
    {
        this.nom = nom;
    }

    public String getNom()
    {
        return this.nom;
    }

    @Override
    public String toString()
    {
        return "nom: " + nom;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof Objet == false)
            return false;
        else
        {
            Objet caseCoude = (Objet) o;
            return this.toString().equals(caseCoude.toString());
        }
    }
}
