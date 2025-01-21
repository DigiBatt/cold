
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InformationModule import Information



from .PureNumberQuantityModule import PureNumberQuantity



from .IntegerModule import Integer







class AtomicNumber(Information, PureNumberQuantity, Integer):
    """
    Class representing the `AtomicNumber` entity, which inherits from:
    - Information, PureNumberQuantity, Integer

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_07de47e0_6bb6_45b9_b55a_4f238efbb105'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AtomicNumber'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AtomicNumber(
    
    class_iri='https://w3id.org/emmo#EMMO_07de47e0_6bb6_45b9_b55a_4f238efbb105',
    
    class_name='AtomicNumber',
    
    iupacReference="example_value",
    
    definition="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_07de47e0_6bb6_45b9_b55a_4f238efbb105',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AtomicNumber',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    