
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity



from .IntensityModule import Intensity







class DensityOfHeatFlowRate(ThermodynamicalQuantity, Intensity):
    """
    Class representing the `DensityOfHeatFlowRate` entity, which inherits from:
    - ThermodynamicalQuantity, Intensity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ee7ddcb8_ad8e_4ff7_a09f_889d8edf8f8b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DensityOfHeatFlowRate'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DensityOfHeatFlowRate(
    
    class_iri='https://w3id.org/emmo#EMMO_ee7ddcb8_ad8e_4ff7_a09f_889d8edf8f8b',
    
    class_name='DensityOfHeatFlowRate',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ee7ddcb8_ad8e_4ff7_a09f_889d8edf8f8b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DensityOfHeatFlowRate',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    