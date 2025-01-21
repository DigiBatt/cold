
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class EnergyPerSquareMagneticFluxDensityUnit(SIDimensionalUnit):
    """
    Class representing the `EnergyPerSquareMagneticFluxDensityUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_df1d3a25_eba2_4530_9803_d82d349f4051'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyPerSquareMagneticFluxDensityUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyPerSquareMagneticFluxDensityUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_df1d3a25_eba2_4530_9803_d82d349f4051',
    
    class_name='EnergyPerSquareMagneticFluxDensityUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_df1d3a25_eba2_4530_9803_d82d349f4051',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyPerSquareMagneticFluxDensityUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    