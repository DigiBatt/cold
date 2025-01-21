
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RestMassModule import RestMass



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity







class NuclidicMass(RestMass, AtomicAndNuclearPhysicsQuantity):
    """
    Class representing the `NuclidicMass` entity, which inherits from:
    - RestMass, AtomicAndNuclearPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_58c08428_03e2_446d_85e1_f94cc6682e2b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NuclidicMass'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NuclidicMass(
    
    class_iri='https://w3id.org/emmo#EMMO_58c08428_03e2_446d_85e1_f94cc6682e2b',
    
    class_name='NuclidicMass',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_58c08428_03e2_446d_85e1_f94cc6682e2b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NuclidicMass',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    