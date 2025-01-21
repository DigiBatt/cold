
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeclaredModule import Declared



from .AtomModule import Atom





from .ChemicalElementModule import ChemicalElement





class FranciumAtom(Declared, Atom):
    """
    Class representing the `FranciumAtom` entity, which inherits from:
    - Declared, Atom

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_291a1550_d4cb_5934_b0db_0ea3c6a23932'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FranciumAtom'`
        - **Alias**: `class_name`
    
    - `hasChemicalSymbol` (`Optional[ChemicalElement]`): 
        - **Default Value**: `None`
        - **Alias**: `hasChemicalSymbol`
    
    - `hasAtomicNumber` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasAtomicNumber`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasIUPAC2016AtomicMass` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasIUPAC2016AtomicMass`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FranciumAtom(
    
    class_iri='https://w3id.org/emmo#EMMO_291a1550_d4cb_5934_b0db_0ea3c6a23932',
    
    class_name='FranciumAtom',
    
    hasChemicalSymbol="example_value",
    
    hasAtomicNumber="example_value",
    
    elucidation="example_value",
    
    hasIUPAC2016AtomicMass="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_291a1550_d4cb_5934_b0db_0ea3c6a23932',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FranciumAtom',
        alias="class_name"
    )
    
    hasChemicalSymbol: Optional[ChemicalElement] = Field(
        None,
        alias="hasChemicalSymbol"
    )
    
    hasAtomicNumber: Optional[str] = Field(
        None,
        alias="hasAtomicNumber"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasIUPAC2016AtomicMass: Optional[str] = Field(
        None,
        alias="hasIUPAC2016AtomicMass"
    )
    

    
    @validator("hasChemicalSymbol", pre=True, always=True)
    def validate_hasChemicalSymbol(cls, value):
        if value is not None and not isinstance(value, ChemicalElement):
            raise ValueError(f"Field 'hasChemicalSymbol' must be an instance of 'ChemicalElement' or its subclass.")
        return value
    
    

    

    