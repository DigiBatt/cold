
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UnitSymbolModule import UnitSymbol



from .SICoherentUnitModule import SICoherentUnit







class SIUnitSymbol(UnitSymbol, SICoherentUnit):
    """
    Class representing the `SIUnitSymbol` entity, which inherits from:
    - UnitSymbol, SICoherentUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_32129fb5_df25_48fd_a29c_18a2f22a2dd5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIUnitSymbol'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIUnitSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_32129fb5_df25_48fd_a29c_18a2f22a2dd5',
    
    class_name='SIUnitSymbol',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_32129fb5_df25_48fd_a29c_18a2f22a2dd5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIUnitSymbol',
        alias="class_name"
    )
    

    
    

    

    