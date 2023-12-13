package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public abstract class Case 
{
    protected String nom; // ligne {- |}, coude {┘ └ ┌ ┐}, triangle {┤ ┴ ├ ┬}
    protected Position position; // position de la case dans le plateau
    protected int rotation; // rotation de la case
    protected Objet objet; // Objet à récupérer
    protected boolean depart;
    protected boolean fixe;

    protected Case()
    {
        this.nom = "test";
        this.position = new Position();
        this.rotation = 0;
        this.objet = null;
        this.depart = false;
        this.fixe = false;
    }

    public Case(String nom, Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        this.nom = nom;
        this.position = position;
        
        if (verifierRotation(rotation))
            this.rotation = rotation;
        else 
            this.rotation = 0;

        this.objet = objet;

        this.depart = depart;
        this.fixe = fixe;
    }

    public Case(Case c)
    {
        this.nom = c.getNom();
        this.position = c.getPosition();
        this.rotation = c.getRotation();
        this.objet = c.getObjet();
        this.depart = c.getDepart();
        this.fixe = c.getFixe();
    }

    // set/get position

    public void setPosition(Position position) {
        this.position = position;
    }

    public Position getPosition() {
        return this.position;
    }

    // set/get rotation
    public void setRotation(int rotation) {
        if (verifierRotation(rotation))
            this.rotation = rotation;
    }

    public int getRotation() {
        return this.rotation;
    }

    // set/get depart
    public void setDepart(boolean depart) {
        this.depart = depart;
    }

    public boolean getDepart()
    {
        return this.depart;
    }

    // set/get fixe
    public void setFixe(boolean fixe)
    {
        this.fixe = fixe;
    }

    public boolean getFixe()
    {
        return this.fixe;
    }

    // set/get objet
    public void setObjet(Objet objet)
    {
        this.objet = objet;
    }

    public Objet getObjet()
    {
        return this.objet;
    }

    public String getNom()
    {
        return this.nom;
    }
    
    protected boolean verifierRotation(int rotation)
    {
        if (rotation == 0 || rotation == 90 || rotation == 180 || rotation == 270)
            return true;
        else 
            return false;
    }

    public abstract Case newInstance();

    public abstract String afficher();

    public abstract ArrayList<Position> getDeplacement();


    @Override
    public String toString()
    {
        return "Case " + this.nom + " " + this.position + " : rotation = " + this.rotation + " | départ = " + this.depart + " | fixe = " + this.fixe + " | objet = " + this.objet; 
    }

    @Override
    public abstract boolean equals(Object o);
}