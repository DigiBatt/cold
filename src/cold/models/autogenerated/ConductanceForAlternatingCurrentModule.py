
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricConductanceModule import ElectricConductance







class ConductanceForAlternatingCurrent(ElectricConductance):
    """
    Class representing the `ConductanceForAlternatingCurrent` entity, which inherits from:
    - ElectricConductance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_01b80fdd_065c_4caf_b36c_4c0724936e24'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConductanceForAlternatingCurrent'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConductanceForAlternatingCurrent(
    
    class_iri='https://w3id.org/emmo#EMMO_01b80fdd_065c_4caf_b36c_4c0724936e24',
    
    class_name='ConductanceForAlternatingCurrent',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_01b80fdd_065c_4caf_b36c_4c0724936e24',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConductanceForAlternatingCurrent',
        alias="class_name"
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    