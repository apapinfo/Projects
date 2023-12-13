package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseCoude extends Case
{
    public CaseCoude()
    {
        super("coude", new Position(), 0, null, false, false);
    }

    public CaseCoude(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("coude", position, rotation, objet, depart, fixe);
    }

    public CaseCoude(CaseCoude c)
    {
        super(c);
    }

    @Override
    public String afficher()
    {
        String contenu = "";
        if (this.rotation == 0)
            contenu = "┘";
        else if (this.rotation == 90)
            contenu = "└";
        else if (this.rotation == 180)
            contenu = "┌";
        else if (this.rotation == 270)
            contenu = "┐";
        
        return contenu;
    }

    public CaseCoude newInstance()
    {
        CaseCoude newCase = new CaseCoude(this);
        return newCase;
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();

        if (this.rotation == 0) // ┘
        {
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche 
            deplacementpossible.add(new Position(this.position.getLongueur(), this.getPosition().getHauteur() - 1)); // en haut
        }
        else if (this.rotation == 90) // └
        {
            deplacementpossible.add(new Position(this.position.getLongueur(), this.getPosition().getHauteur() - 1)); // en haut
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite
        }
        else if  (this.rotation == 180) // ┌
        {
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite
            deplacementpossible.add(new Position(this.position.getLongueur(), this.getPosition().getHauteur() + 1)); // en bas
        }
        else if (this.rotation == 270) // ┐
        {
            deplacementpossible.add(new Position(this.position.getLongueur(), this.getPosition().getHauteur() + 1)); // en bas
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
        }

        return deplacementpossible;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseCoude == false)
            return false;
        else
        {
            CaseCoude caseCoude = (CaseCoude) o;
            return this.toString().equals(caseCoude.toString());
        }
    }
}