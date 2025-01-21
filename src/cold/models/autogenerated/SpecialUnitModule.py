
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .UnitSymbolModule import UnitSymbol







class SpecialUnit(DerivedUnit, UnitSymbol):
    """
    Class representing the `SpecialUnit` entity, which inherits from:
    - DerivedUnit, UnitSymbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3ee80521_3c23_4dd1_935d_9d522614a3e2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpecialUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpecialUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3ee80521_3c23_4dd1_935d_9d522614a3e2',
    
    class_name='SpecialUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3ee80521_3c23_4dd1_935d_9d522614a3e2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpecialUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    