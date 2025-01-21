
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalBosonModule import FundamentalBoson







class HiggsBoson(FundamentalBoson):
    """
    Class representing the `HiggsBoson` entity, which inherits from:
    - FundamentalBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_676a29e6_d4e1_4b54_8961_25947bd20861'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HiggsBoson'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HiggsBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_676a29e6_d4e1_4b54_8961_25947bd20861',
    
    class_name='HiggsBoson',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_676a29e6_d4e1_4b54_8961_25947bd20861',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HiggsBoson',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    