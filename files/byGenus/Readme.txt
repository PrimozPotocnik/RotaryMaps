This is a short description of the magma code that imports the database of all rotary maps (orientable reflexible,
non-orientable reflexible and chiral) of genera between 2 and 1501 (for the orienatble maps) and 3 and 1502 (for 
non-orientable maps)


//
// Orientable reflexible maps
//

* load "ImportOrientableReflexibleMapsGenus1501.mgm";

  Requires also: OrientableReflexibleGenus1501-rels.txt, OrientableReflexibleGenus1501-data.csv

  Loads the the reflexible (regular) maps on orientable surfaces of genus g, 2\le g \le 1501.
  For now, only the following commands are available.

* OrientableReflexibleMapOfName(ID)

  For ID being one of the names of an orientable reflexible maps (such as "R14.12"),
  constructs a finitely presented group on 3 generators: R,S and T with T inverting R and S.
  Here R is intepretated as a rotation around a face and S as a rotation around an incident vertex.
  If "*" is added to the ID, then the dual is returned.

* IDsOfReflexibleOrientableMapsOfGenus(g)

  For a positive integer g > 2, returns IDs for all non-orientable regular maps up to genus g,
  including the IDs that end with "*". When these IDs are passed to NonOrientableMapOfName(ID),
  all maps of that genus are returned (including the duals). The IDs have the form "R<g>.<k>" where
  g is the genus of the map and k is the index of that map within all of that genus (up to duals). 
  The ID of the dual of the map "R<g>.<k>" is denoted by "R<g>.<k>*".

* NumberOfReflexibleOrientableMapsOfGenus(g)

  Returns the number of relfexible orientable of genus g, for 2 \le g \le 1501.   

* GenusOfReflexibleOrientableMap(ID);

  For ID being one of the names of an orientable reflexible maps (such as "R14.12"), returns the genus of that map.

* TypeOfReflexibleOrientableMap(ID)

   Returns the triple [p,q,r] where p is the face-length, q is the valence and r is the lingth
   of the Petrie walk.

* NumberOfVerticesOfReflexibleOrientableMap(ID);

   Returns the number of vertices of the map with the name ID.

* NumberOfEdgesOfReflexibleOrientableMap(ID);

   Returns the number of edges of the map with the name ID.

* NumberOfFacesOfReflexibleOrientableMap(ID);

   Returns the number of faces of the map with the name ID.

* MultiplicityOfReflexibleOrientableMap(ID);

  Returns the pair [mV,mF] where mV is the vertex-multiplicity (i.e. the number of edges
  between two adjacent vertices) and mF is mV in the dual (that is, the number of edges shared by
  two adjacent faces).

* WilsonInvarianceOfReflexibleOrientableMap(ID)

  Returns one of the strings "I", "I+D", "I+P", "I+DPD", "I+DP+PD", "All",
  meaining that the map with the name being ID is invariant under identiti only,
  duality, Petrie duality, Opposite, PetrieDual or all of the Wilson operations on the maps.


SizeOfHoleClassOfReflexibleOrientableMap(ID);

  Given the name ID of a reflexible orientable map M of valence q, returns the number of multipliers t in Z_q^*
  such that the t-hole-map of M is isomorphic to M.

//
// Non-orientable reflexible maps
//

* load "ImportNonOrientableMapsGenus1502.mgm";

   Requires also: NonorientableGenus1502-rels.txt, NonorientableGenus1502-data.csv
 
   Loads the regular (rotary) maps on non-orientable surfaces of genera g, 3\le g \le 1502.
   The following commands become available after loading:

* NonOrientableMapOfName(ID)

  For ID being one of the names of a non-orientable reflexible maps (such as "N64.4"),
  constructs a finitely presented group on 3 generators: R,S and T with T inverting R and S,
  R rotating around a face and S rotatin around a vertex.
  If "*" is added to the ID, then the dual is returned.

* IDsOfNonOrientableMapsOfGenus(g)

   For a positive integer g > 2, returns IDs for all non-orientable regular maps up to genus g,
   including the IDs that end with "*". When these IDs are passed to NonOrientableMapOfName(ID),
   all maps on that genus are returned (including the duals).

* NumberOfNonOrientableMapsOfGenus(g)

   Returns the number of non-orientable regular maps of genus g.

* GenusOfNonOrientableMap(ID);

   Returns the genus of the non-orientable regular map with the name ID.

* TypeOfNonOrientableMap(ID)

   Returns the triple [p,q,r] where p is the face-length, q is the valence and r is the lingth
   of the Petrie walk.

* NumberOfVerticesOfNonOrientableMap(ID);

   Returns the number of vertices of the non-orientable regular map with the name ID.

* NumberOfEdgesOfNonOrientableMap(ID);

   Returns the number of edges of the non-orientable regular map with the name ID.

* NumberOfFacesOfNonOrientableMap(ID);

   Returns the number of faces of the non-orientable regular map with the name ID.

* MultiplicityOfNonOrientableMap(ID);

  Returns the pair [mV,mF] where mV is the vertex-multiplicity (i.e. the number of edges
  between two adjacent vertices) and mF is mV in the dual.

* WilsonInvarianceOfNonOrientableMap(ID)

  Returns one of the strings "I", "I+D", "I+P", "I+DPD", "I+DP+PD", "All",
  meaining that the map with the name being ID is invariant under identiti only,
  duality, Petrie duality, Opposite, PetrieDual or all of the Wilson operations on the maps.

SizeOfHoleClassOfNonOrientableMap(ID);

  The number of the maps that are a j-hole of the map with ID for some j coprime to the valence.

//
// Chiral maps
//

* load "ImportChiralMapsGenus1501.mgm";

   Requires also files: ChiralGenus1501-rels.txt, ChiralGenus1501-data.csv 
 
   Loads chiral rotary maps on orientable surfaces of genera g, 2\le g \le 1501.
   The following commands become available upon loading:
   
 * ChiralMapOfName(ID)

    Given an ID of a chiral map (say "C10.2" or "C10.2*"), returns a FPgroup G 
    generated by two generators R:=G.1 and S:=G.2, where R is
    a rotation about the centre of a face and S is a rotation around a vertex.
    The symbol "*" in the ID indicates that the map is the dual of the one
    whose ID has no "*".

 * IDsOfChiralMapsOfGenus(g)

   For a given genus g, returns all the IDs of the chiral maps of genus g.

 * NumberOfChiralMapsOfGenus(g)

   Returns the number of chiral maps of genus g.

 * GenusOfChiralMap(ID);

   Returns the genus of the map with the name being ID.

 * TypeOfChiralMap(ID);

    Returns [p,q,r] of the map with the name being ID.

 * NumberOfVerticesOfChiralMap(ID)

    Returns the number of vertices of the map with the name being ID.

 * NumberOfEdgesOfChiralMap(ID)

    Returns the edges of vertices of the map with the name being ID.

 * NumberOfFacesOfChiralMap(ID)

    Returns the number of faces of the map with the name being ID.

 * MultiplicityOfChiralMap(ID)

  Returns the pair [mV,mF] where mV is the vertex-multiplicity (i.e. the number of edges
  between two adjacent vertices) and mF is mV in the dual.

 * WilsonInvarianceOfChiralMap(ID)

   Returns one of the strings: Four (invariant under none), SD, MSD.
   depending on which "Wilson operations" it is invariant under.

 * SizeOfHoleClassOfChiralMap(ID)

  The number of the maps that are a j-hole of the map with ID for some j coprime to the valence.