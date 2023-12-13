package labyrinthe.core.ia;

import labyrinthe.core.Joueur;
import labyrinthe.core.Plateau;
import labyrinthe.core.Position;
import labyrinthe.core.cases.Case;

public abstract class Ia 
{
    private String nom;
    private String description;

    protected Ia()
    {
        this.nom = "D.U.M.M.I.E";
        this.description = "Digital Utility Mock Man Intelligent Example";
    }

    protected Ia(String nom, String description)
    {
        this.nom = nom;
        this.description = description;
    }

    public void setNom(String nom)
    {
        this.nom = nom;
    }

    public String getNom()
    {
        return this.nom;
    }

    public void setDescription(String desc)
    {
        this.description = desc;
    }

    public String getDescription()
    {
        return this.description;
    }

    public abstract int rotationCase(Case c);
    public abstract Position deplacementCase(Plateau plateau, Joueur joueur);
    public abstract Position deplacementJoueur(Plateau plateau, Joueur joueur);
}