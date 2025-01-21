
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalSymbolicConstructModule import ChemicalSymbolicConstruct



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation



from .SymbolicConstructModule import SymbolicConstruct



from .ChemicalModule import Chemical







class ChemicalComposition(ChemicalSymbolicConstruct, SpatioTemporalTessellation, SymbolicConstruct, Chemical):
    """
    Class representing the `ChemicalComposition` entity, which inherits from:
    - ChemicalSymbolicConstruct, SpatioTemporalTessellation, SymbolicConstruct, Chemical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7efd64d1_05a1_49cd_a7f0_783ca050d4f3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalComposition'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalComposition(
    
    class_iri='https://w3id.org/emmo#EMMO_7efd64d1_05a1_49cd_a7f0_783ca050d4f3',
    
    class_name='ChemicalComposition',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7efd64d1_05a1_49cd_a7f0_783ca050d4f3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalComposition',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    