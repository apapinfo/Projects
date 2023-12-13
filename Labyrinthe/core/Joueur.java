package labyrinthe.core;
import labyrinthe.core.cases.*;
import labyrinthe.core.ia.Ia;
import labyrinthe.core.objets.*;

import java.util.ArrayList;

public class Joueur
{
    private static int count = 1;
    private final int id;
    private String nom;
    private Position position;
    private ArrayList<Objet> paquetCartes;

    private Ia ia;

    // n'a pas d'interet sauf pour le terminal
    // Reset couleur
    public static final String ANSI_RESET = "\u001B[0m";
  
    // 4 couleurs (pas très utile d'en faire plus vu que c'est que pour le terminal)
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_GREEN = "\u001B[32m";

    // le fond des 4 couleurs
    public static final String ANSI_RED_BACKGROUND = "\u001B[41m";
    public static final String ANSI_BLUE_BACKGROUND = "\u001B[44m";
    public static final String ANSI_YELLOW_BACKGROUND = "\u001B[43m";
    public static final String ANSI_GREEN_BACKGROUND = "\u001B[42m";

    public Joueur()
    {
        this.id = count++;
        this.nom = "M.A.C.H.I.N"; // pour faire long : "Manequin Artificiel Conscient Humanoide Instructeur de Néophytes"
        this.position = null;
        this.paquetCartes = new ArrayList<Objet>();

        //this.ia = new Dummy();
    }

    public Joueur(String nom, Position position)
    {
        this.id = count++;
        this.nom = nom;
        this.position = position;
        this.paquetCartes = new ArrayList<Objet>();
        this.ia = null;
    }

    public Joueur(String nom, Position position, Ia ia)
    {
        this.id = count++;
        this.nom = nom;
        this.position = position;
        this.paquetCartes = new ArrayList<Objet>();

        this.ia = ia;
    }

    // get Index du joueur

    public int getIndex()
    {
        return this.id;
    }

    // set/get Nom du joueur

    public void setNom(String nom)
    {
        this.nom = nom;
    }

    public String getNom()
    {
        return this.nom;
    }

    // set/get position

    public void setPosition(Position position)
    {
        this.position = position;
    }

    public Position getPosition()
    {
        return this.position;
    }

    // add/get paquetCartes
    public void addObjet(Objet o)
    {
        this.paquetCartes.add(o);
    }

    public ArrayList<Objet> getPaquetCarte()
    {
        return this.paquetCartes;
    }

    public void setIa(Ia ia)
    {
        this.ia = ia;
    }

    public Ia getIa()
    {
        return this.ia;
    }

    public ArrayList<Position> getDeplacementPossible(ArrayList<Case> plateau)
    {
        Case casedepart = checkCase(plateau, this.position);
        ArrayList<Position> deplacementDepart = new ArrayList<Position>();
        ArrayList<Position> deplacementPossible = new ArrayList<Position>();

        if (casedepart.getDeplacement() != null)
        {
            deplacementDepart = casedepart.getDeplacement();

            deplacementPossible.addAll(checkDeplacement(plateau, casedepart.getPosition(), deplacementDepart));
        }

        return deplacementPossible;
    }

    public ArrayList<Position> getToutDeplacementPossible(ArrayList<Case> plateau)
    {
        Case casedepart = checkCase(plateau, this.position);
        ArrayList<Position> deplacementDepart = new ArrayList<Position>();
        ArrayList<Position> deplacementPossible = new ArrayList<Position>();

        if (casedepart.getDeplacement() != null)
        {
            deplacementDepart = casedepart.getDeplacement();

            deplacementPossible.addAll(checkDeplacement(plateau, casedepart.getPosition(), deplacementDepart));

            int i = 0;
            while (i < deplacementPossible.size())
            {
                Case casesuivante = checkCase(plateau, deplacementPossible.get(i));
                if (casesuivante.getDeplacement() != null)
                {
                    ArrayList<Position> nouveauDeplacementPossible= new ArrayList<Position>();
                    nouveauDeplacementPossible.addAll(checkDeplacement(plateau, casesuivante.getPosition(), casesuivante.getDeplacement()));
                    for (int j = 0; j < nouveauDeplacementPossible.size(); j++)
                        if (!deplacementPossible.contains(nouveauDeplacementPossible.get(j)))
                            deplacementPossible.add(nouveauDeplacementPossible.get(j));
                }
                i++;
            }
        }
        
        return deplacementPossible; 
    }

    // cherche la case de la position donné
    private Case checkCase(ArrayList<Case> plateau, Position p)
    {
        int indexCase = -1;
        for (int i = 0; i < plateau.size(); i++)
            if (plateau.get(i).getPosition().equals(p))
                indexCase = i;
        
        if (indexCase == -1)
            return null;
        else
            return plateau.get(indexCase);
    }

    private ArrayList<Position> checkDeplacement(ArrayList<Case> plateau, Position position, ArrayList<Position> deplacement)
    {
        ArrayList<Position> deplacementPossible = new ArrayList<Position>();

        for (int i = 0; i < plateau.size(); i++)
            for (int j = 0; j < deplacement.size(); j++)
                if (plateau.get(i).getPosition().equals(deplacement.get(j)))
                    if (plateau.get(i).getDeplacement() != null)
                        if (plateau.get(i).getDeplacement().contains(position))
                            deplacementPossible.add(plateau.get(i).getPosition());
        
        return deplacementPossible;
    }

    public boolean deplacer(ArrayList<Case> plateau, Position p)
    {
        ArrayList<Position> listeDeplacementPossible = new ArrayList<Position>();
        listeDeplacementPossible = getToutDeplacementPossible(plateau);

        if (listeDeplacementPossible.contains(p))
            this.position = p;
        else
            if (!p.equals(this.position))
                return false;
        
        return true;
    }

    public void aRecupererObjet()
    {
        this.paquetCartes.remove(0);
    }

    public Boolean recupererToutObjet()
    {
        Boolean fini = false;
        
        if (this.paquetCartes.size() == 0)
            fini = true;
        
        return fini;
    }

    // utile que pour le terminal
    public String getCouleur()
    {
        String couleur = "\u001B[37m";

        switch (this.id)
        {
            case 1:
                couleur = ANSI_RED;
                break;
            case 2:
                couleur = ANSI_BLUE;
                break;
            case 3:
                couleur = ANSI_YELLOW;
                break;
            case 4:
                couleur = ANSI_GREEN;
                break;
            default:
                couleur = "\u001B[37m";
        }

        return couleur;
    }

    public String getCouleurFond()
    {
        String couleur = "\u001B[40m";

        switch (this.id)
        {
            case 1:
                couleur = ANSI_RED_BACKGROUND;
                break;
            case 2:
                couleur = ANSI_BLUE_BACKGROUND;
                break;
            case 3:
                couleur = ANSI_YELLOW_BACKGROUND;
                break;
            case 4:
                couleur = ANSI_GREEN_BACKGROUND;
                break;
            default:
                couleur = "\u001B[40m";
        }

        return couleur;
    }

    @Override
    public String toString()
    {
        // pour une meilleur visibilté lors du jeu en mode terminal
        String couleur = getCouleur();

        return couleur + "Joueur n°" + this.id + " : " + this.nom + ", position = " + this.position + ANSI_RESET;
    }
}