package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseT extends Case
{
    public CaseT()
    {
        super("T", new Position(), 0, null, false, false);
    }

    public CaseT(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("T", position, rotation, objet, depart, fixe);
    }

    public CaseT(CaseT c)
    {
        super(c);
    }

    public CaseT newInstance()
    {
        CaseT newCase = new CaseT(this);
        return newCase;
    }

    @Override
    public String afficher() 
    {
        String contenu = "";
        if (this.rotation == 0)
            contenu = "┤";
        else if (this.rotation == 90)
            contenu = "┴";
        else if (this.rotation == 180)
            contenu = "├";
        else if (this.rotation == 270)
            contenu = "┬";
        
        return contenu;
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();

        if (this.rotation == 0) // ┤
        {
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() - 1)); // en haut
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() + 1)); // en bas
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
        }
        else if (this.rotation == 90) // ┴
        {
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() - 1)); // en haut
        }
        else if (this.rotation == 180) // ├
        {
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() - 1)); // en haut
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() + 1)); // en bas
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite
        }
        else if (this.rotation == 270) // ┬
        {
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() + 1)); // en bas
        }

        return deplacementpossible;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseT == false)
            return false;
        else
        {
            CaseT caseT = (CaseT) o;
            return this.toString().equals(caseT.toString());
        }
    }
}