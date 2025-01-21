
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuantumNumberModule import QuantumNumber







class SpinQuantumNumber(QuantumNumber):
    """
    Class representing the `SpinQuantumNumber` entity, which inherits from:
    - QuantumNumber

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1a5dd75a_6ed6_4148_a99c_001a27f5b417'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpinQuantumNumber'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
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
    obj = SpinQuantumNumber(
    
    class_iri='https://w3id.org/emmo#EMMO_1a5dd75a_6ed6_4148_a99c_001a27f5b417',
    
    class_name='SpinQuantumNumber',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1a5dd75a_6ed6_4148_a99c_001a27f5b417',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpinQuantumNumber',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
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
    

    
    

    

    