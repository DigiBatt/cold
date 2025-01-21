
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalSpeciesModule import ChemicalSpecies



from .ChemicalSymbolModule import ChemicalSymbol



from .SymbolModule import Symbol



from .ChemicalModule import Chemical







class ChemicalElement(ChemicalSpecies, ChemicalSymbol, Symbol, Chemical):
    """
    Class representing the `ChemicalElement` entity, which inherits from:
    - ChemicalSpecies, ChemicalSymbol, Symbol, Chemical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4f40def1_3cd7_4067_9596_541e9a5134cf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalElement'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalElement(
    
    class_iri='https://w3id.org/emmo#EMMO_4f40def1_3cd7_4067_9596_541e9a5134cf',
    
    class_name='ChemicalElement',
    
    iupacReference="example_value",
    
    hasSymbolValue="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4f40def1_3cd7_4067_9596_541e9a5134cf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalElement',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    