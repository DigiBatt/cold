
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagneticFluxDensityModule import MagneticFluxDensity







class MagneticPolarisation(MagneticFluxDensity):
    """
    Class representing the `MagneticPolarisation` entity, which inherits from:
    - MagneticFluxDensity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_74a096dd_cc83_4c7e_b704_0541620ff18d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagneticPolarisation'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagneticPolarisation(
    
    class_iri='https://w3id.org/emmo#EMMO_74a096dd_cc83_4c7e_b704_0541620ff18d',
    
    class_name='MagneticPolarisation',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_74a096dd_cc83_4c7e_b704_0541620ff18d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagneticPolarisation',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    