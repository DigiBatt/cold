
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicConstructModule import SymbolicConstruct



from .ChemicalModule import Chemical







class ChemicalSymbolicConstruct(SymbolicConstruct, Chemical):
    """
    Class representing the `ChemicalSymbolicConstruct` entity, which inherits from:
    - SymbolicConstruct, Chemical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bd8db028_aec2_4a44_ad93_1a9f8270f72c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalSymbolicConstruct'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalSymbolicConstruct(
    
    class_iri='https://w3id.org/emmo#EMMO_bd8db028_aec2_4a44_ad93_1a9f8270f72c',
    
    class_name='ChemicalSymbolicConstruct',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bd8db028_aec2_4a44_ad93_1a9f8270f72c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalSymbolicConstruct',
        alias="class_name"
    )
    

    
    

    

    