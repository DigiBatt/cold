
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoefficientOfThermalExpansionModule import CoefficientOfThermalExpansion



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity







class LinearExpansionCoefficient(CoefficientOfThermalExpansion, ThermodynamicalQuantity):
    """
    Class representing the `LinearExpansionCoefficient` entity, which inherits from:
    - CoefficientOfThermalExpansion, ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_399426d1_c4cc_414c_806f_47096c72d634'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LinearExpansionCoefficient'`
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
    obj = LinearExpansionCoefficient(
    
    class_iri='https://w3id.org/emmo#EMMO_399426d1_c4cc_414c_806f_47096c72d634',
    
    class_name='LinearExpansionCoefficient',
    
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
        'https://w3id.org/emmo#EMMO_399426d1_c4cc_414c_806f_47096c72d634',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LinearExpansionCoefficient',
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
    

    
    

    

    