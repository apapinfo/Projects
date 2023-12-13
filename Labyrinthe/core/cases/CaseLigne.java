package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseLigne extends Case
{
    public CaseLigne()
    {
        super("ligne", new Position(), 0, null, false, false);
    }

    public CaseLigne(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("ligne", position, rotation, objet, depart, fixe);
    }

    public CaseLigne(CaseLigne c)
    {
        super(c);
    }

    @Override
    public String afficher()
    {
        String contenu = "";
        if (this.rotation == 0 || this.rotation == 180)
            contenu =  "-";
        else if (this.rotation == 90 || this.rotation == 270)
            contenu = "|";
        
        return contenu;
    }

    public CaseLigne newInstance()
    {
        CaseLigne newCase = new CaseLigne(this);
        return newCase;
    }


    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();

        if (this.rotation == 0 || this.rotation == 180) // -
        {
            deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
            deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite
        }
        else if (this.rotation == 90 || this.rotation == 270) // |
        {
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() - 1)); // en haut
            deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() + 1)); // en bas
        }

        return deplacementpossible;
    }

    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseLigne == false)
            return false;
        else
        {
            CaseLigne caseLigne = (CaseLigne) o;
            return this.toString().equals(caseLigne.toString());
        }
    }
}